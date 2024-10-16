// @generated by protobuf-ts 2.9.4 with parameter generate_dependencies,optimize_code_size
// @generated from protobuf file "helloworld/v1/service.proto" (package "helloworld.v1", syntax proto3)
// tslint:disable
import type { RpcTransport } from "@protobuf-ts/runtime-rpc";
import type { ServiceInfo } from "@protobuf-ts/runtime-rpc";
import { HelloWorldService } from "./service";
import { stackIntercept } from "@protobuf-ts/runtime-rpc";
import type { HelloWorldResponse } from "./service";
import type { HelloWorldRequest } from "./service";
import type { UnaryCall } from "@protobuf-ts/runtime-rpc";
import type { RpcOptions } from "@protobuf-ts/runtime-rpc";
/**
 * @generated from protobuf service helloworld.v1.HelloWorldService
 */
export interface IHelloWorldServiceClient {
    /**
     * @generated from protobuf rpc: HelloWorld(helloworld.v1.HelloWorldRequest) returns (helloworld.v1.HelloWorldResponse);
     */
    helloWorld(input: HelloWorldRequest, options?: RpcOptions): UnaryCall<HelloWorldRequest, HelloWorldResponse>;
}
/**
 * @generated from protobuf service helloworld.v1.HelloWorldService
 */
export class HelloWorldServiceClient implements IHelloWorldServiceClient, ServiceInfo {
    typeName = HelloWorldService.typeName;
    methods = HelloWorldService.methods;
    options = HelloWorldService.options;
    constructor(private readonly _transport: RpcTransport) {
    }
    /**
     * @generated from protobuf rpc: HelloWorld(helloworld.v1.HelloWorldRequest) returns (helloworld.v1.HelloWorldResponse);
     */
    helloWorld(input: HelloWorldRequest, options?: RpcOptions): UnaryCall<HelloWorldRequest, HelloWorldResponse> {
        const method = this.methods[0], opt = this._transport.mergeOptions(options);
        return stackIntercept<HelloWorldRequest, HelloWorldResponse>("unary", this._transport, method, opt, input);
    }
}
